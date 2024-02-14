Command for generating embeddings and saving them to disk

    python generate_embeddings.py --output_data_path embeddings_db.pkl

Command for generating completions using end-to-end RAG

    python simple_RAG.py --embeddings_database_path embeddings_db.pkl --query_csv_pa
    th data/golden_records_questions.csv --top_k 5 --output_file_path results/v2_golden_record_end_to_end_five_shot.csv --sc
    hema_desc_path descriptions_text.txt

Command for generating metrics for a given results file

    python process_dataset_metrics.py --results_path results/v2_golden_record_end_to_e
    nd_five_shot.csv
