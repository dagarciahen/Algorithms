import argparse
import json
import random
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = PROJECT_ROOT/"leetcode-problems"/"problems"

def load_problems():
    path = Path(__file__).resolve().parent / "leetcode-problems" / "merged_problems.json"

    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list) and (
                not value or isinstance(value[0], dict)
            ):
                if value and "title" in value[0]:
                    return value

        if "title" in data and "problem_id" in data:
            return [data]

    raise ValueError("Unexpected structure in merged_problems.json")


def format_problem(problem):
    title = f'#{problem["problem_id"]} - {problem["title"]}'
    difficulty = f'Difficulty: {problem.get("difficulty", "Unknown")}'

    topics = problem.get("topics", [])
    if isinstance(topics, list):
        topics = ", ".join(topics)
    topics_line = f"Topics: {topics}"

    description = problem.get("description", "")
    statement = description.split("Example 1:", 1)[0].strip()

    doc_lines = [
        title,
        difficulty,
        topics_line,
        "",
        statement,
    ]

    examples = problem.get("examples", [])
    for i, example in enumerate(examples, start=1):
        doc_lines.extend([
            "",
            f"Example {i}:",
            example.get("example_text", str(example)),
        ])

    constraints = problem.get("constraints", [])
    if constraints:
        doc_lines.extend(["", "Constraints:"])
        doc_lines.extend(f"- {constraint}" for constraint in constraints)

    starter_code = (
        problem.get("code_snippets", {}).get("python3", "")
    )

    return (
        '"""\n'
        + "\n".join(doc_lines)
        + '\n"""\n\n'
        + "from typing import List\n\n"
        + starter_code
    )

def main():
    parser = argparse.ArgumentParser(
        description="Practice LeetCode problems offline"
    )
    parser.add_argument("--topic", help="Topic, e.g. Array or Tree")
    parser.add_argument(
        "--difficulty",
        choices=["Easy", "Medium", "Hard"],
        help="Problem difficulty",
    )
    parser.add_argument("--hint", type=int, help="Show a numbered hint")
    parser.add_argument("--list-topics", action="store_true")
    args = parser.parse_args()

    problems = load_problems()

    if not problems:
        print(f"No problems found in: {PROBLEMS_DIR}")
        return

    if args.list_topics:
        topics = sorted({
            topic
            for problem in problems
            for topic in problem.get("topics", [])
        })
        print("\n".join(topics))
        return

    if args.topic:
        problems = [
            p for p in problems
            if any(args.topic.lower() in topic.lower()
                   for topic in p.get("topics", []))
        ]

    if args.difficulty:
        problems = [
            p for p in problems
            if p.get("difficulty", "").lower()
            == args.difficulty.lower()
        ]

    if not problems:
        print("No problems match those filters.")
        return

    problem = random.choice(problems)

    print(f'\n#{problem["problem_id"]} - {problem["title"]}')
    print(f'Difficulty: {problem.get("difficulty", "Unknown")}')
    print(f'Topics: {", ".join(problem.get("topics", []))}')
    print(f'\n{problem.get("description", "")}')

    for example in problem.get("examples", []):
        print(f'\nExample {example.get("example_num", "")}')
        print(example.get("example_text", ""))

    if args.hint is not None:
        hints = problem.get("hints", [])
        index = args.hint - 1

        if 0 <= index < len(hints):
            print(f'\nHint {args.hint}:')
            print(hints[index])
        else:
            print(f'Hint unavailable. Available hints: {len(hints)}')

    snippets = problem.get("code_snippets", {})
    print("\n--- Python starter code ---")
    print(snippets.get("python3", "# No Python starter code available"))




if __name__ == "__main__":
    main()

