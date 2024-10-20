import json
import leetscrape
from tqdm import tqdm


def main():
    ls = leetscrape.GetQuestionsList()
    ls.scrape()

    df = ls.questions

    # Print all categorySlugs
    fetchLimit = 50

    filtered = df[
        (df['difficulty'] == 'Easy')
        & (df['paidOnly'] == False)
        & (df['acceptanceRate'] < 60)
        & (df['acceptanceRate'] > 40)
        & (df['categorySlug'] == 'algorithms')
    ][:fetchLimit]

    result = []

    for _, row in tqdm(filtered.iterrows(), total=fetchLimit):
        question = leetscrape.GetQuestion(row['titleSlug']).scrape()
        signature = question.Code

        # Remove class definition and outdent the code by 1 level if it's indented
        signature = signature.replace("class Solution:", "")
        signature = "\n".join([line[4:] if line.startswith("    ") else line for line in signature.split("\n")]).strip()

        questionObj = {
            "id": len(result),
            "title": question.title,
            "description": question.Body,
            "signature": signature,
            "test_cases": [],
            "expected_outputs": [],
            "compare_func": "",
        }

        result.append(questionObj)

        with open("database_raw.json", "w") as f:
            json.dump({"CHALLENGES": result}, f, indent=4)


if __name__ == '__main__':
    main()
