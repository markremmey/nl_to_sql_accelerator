1. Gather sample questions and answers

2. Extract Schema from SQL DB - may need to be updated depending on customer scenario. The purpose of this step is to extract a schema description into a .txt file to be used as context for LLM calls for SQL generation.

   `python extract_descriptions.py`

3. Generate embeddings 

    python generate_ai_search_vectors.py

4. Command for generating completions using end-to-end RAG

    python simple_RAG.py --embeddings_database_path embeddings_db.pkl --query_csv_path data/golden_records_questions.csv --top_k 5 --output_file_path results/v2_golden_record_end_to_end_five_shot.csv --schema_desc_path descriptions_text.txt

5. Command for generating metrics for a given results file

    python process_dataset_metrics.py --results_path results/v2_golden_record_end_to_end_five_shot.csv

# TO DO
- Update naming (golden_records --> sql_query_examples)
