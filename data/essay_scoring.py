import csv
import json

def main():
    input_file = 'output.csv'
    output_file = 'scored_output.json'
    
    rows = []
    with open(input_file, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for i, row in enumerate(csvreader):
            rows.append(row)
    
    scored_data = []
    for row in rows:
        print(f"Output: {row['Output']}")
        while True:
            try:
                score = int(input("Enter an integer score: "))
                break
            except ValueError:
                print("Please enter a valid integer.")
        
        scored_data.append({
            'prompt': row['Prompt'],
            'essay': row['Output'],
            'score': score
        })
    
    with open(output_file, 'w') as jsonfile:
        json.dump(scored_data, jsonfile, indent=4)
    
    print(f"Scored data saved to {output_file}")

if __name__ == "__main__":
    main()
