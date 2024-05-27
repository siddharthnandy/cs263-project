import json
import pandas as pd
from eval.metrics import get_stats

data_file = 'data/full_data.json'
human_score_key = 'score'
gpt_score_key = 'gpt_score'
gptft_score_key = 'gptft_score'


def main():
    print(f"Reading {data_file}...")
    with open(data_file) as file:
        data = json.load(file)

    print(f"Parsing JSON into pandas...")
    df = pd.DataFrame(data)
    df_patience = df[df['prompt'].str.startswith("Prompt: Write")]
    df_laughter = df[df['prompt'].str.startswith("Prompt: We")]
    df_resilience = df[df['prompt'].str.startswith("Prompt: Resilience")]

    print(f"Calculating stats...")
    patience_stats_gpt = get_stats(df_patience[human_score_key], df_patience[gpt_score_key])
    patience_stats_gptft = get_stats(df_patience[human_score_key], df_patience[gptft_score_key])
    laughter_stats_gpt = get_stats(df_laughter[human_score_key], df_laughter[gpt_score_key])
    laughter_stats_gptft = get_stats(df_laughter[human_score_key], df_laughter[gptft_score_key])
    resilience_stats_gpt = get_stats(df_resilience[human_score_key], df_resilience[gpt_score_key])
    resilience_stats_gptft = get_stats(df_resilience[human_score_key], df_resilience[gptft_score_key])

    print("---Stats---")
    print("Patience GPT")
    for stat, val in patience_stats_gpt.items():
        print(f"\t{stat}\t{val:.4f}")
    print("Patience GPT FT")
    for stat, val in patience_stats_gptft.items():
        print(f"\t{stat}\t{val:.4f}")
    print("Laughter GPT")
    for stat, val in laughter_stats_gpt.items():
        print(f"\t{stat}\t{val:.4f}")
    print("Laughter GPT FT")
    for stat, val in laughter_stats_gptft.items():
        print(f"\t{stat}\t{val:.4f}")
    print("Resilience GPT")
    for stat, val in resilience_stats_gpt.items():
        print(f"\t{stat}\t{val:.4f}")
    print("Resilience GPT FT")
    for stat, val in resilience_stats_gptft.items():
        print(f"\t{stat}\t{val:.4f}")


if __name__ == "__main__":
    main()