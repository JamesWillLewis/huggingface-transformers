from transformers import pipeline

# use apple metal
DEVICE = 'mps'
MODEL = 'distilbert/distilbert-base-uncased-finetuned-sst-2-english'
def main():
    classifier = pipeline("sentiment-analysis", model=MODEL, device=DEVICE)
    print(classifier("We are very happy to show you the 🤗 Transformers library."))


if __name__ == "__main__":
    # execute only if run as a script
    main()
