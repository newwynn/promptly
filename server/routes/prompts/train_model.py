import argparse
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import load_dataset
import os

def preprocess_function(examples, tokenizer, max_input_length=512, max_target_length=128):
    inputs = examples["input"]
    targets = examples["target"]
    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, padding="max_length")
    labels = tokenizer(targets, max_length=max_target_length, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

def main():
    parser = argparse.ArgumentParser(description="Fine-tune FLAN-T5-Large for prompt enhancement.")
    parser.add_argument('--train_csv', type=str, required=True, help='Path to training CSV file')
    parser.add_argument('--val_csv', type=str, required=True, help='Path to validation CSV file')
    parser.add_argument('--output_dir', type=str, default='./fine-tuned-flan-t5-large', help='Output directory for model')
    parser.add_argument('--epochs', type=int, default=3, help='Number of training epochs')
    parser.add_argument('--batch_size', type=int, default=2, help='Batch size per device')
    parser.add_argument('--lr', type=float, default=2e-5, help='Learning rate')
    args = parser.parse_args()

    model_name = "google/flan-t5-large"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    data_files = {"train": args.train_csv, "validation": args.val_csv}
    dataset = load_dataset("csv", data_files=data_files)

    def preprocess(examples):
        return preprocess_function(examples, tokenizer)

    tokenized_datasets = dataset.map(preprocess, batched=True)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        evaluation_strategy="epoch",
        learning_rate=args.lr,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        num_train_epochs=args.epochs,
        weight_decay=0.01,
        save_total_limit=2,
        fp16=True,
        push_to_hub=False,
        logging_dir=os.path.join(args.output_dir, "logs"),
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
    )

    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print(f"Model and tokenizer saved to {args.output_dir}")

if __name__ == "__main__":
    main()
