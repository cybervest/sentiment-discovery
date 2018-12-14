#! /bin/bash
python -m multiproc pretrain.py --tokenizer-type SentencePieceTokenizer --tokenizer-path ama_32k_tokenizer.model --vocab-size 32000 --data ./data/amazon/reviews.json --text-key reviewText --label-key overall --loose-json --lazy --split 1000,1,1 --distributed-backend nccl --fp16 --dynamic-loss-scale --seq-length 64 --decoder-layers 12  --decoder-embed-dim 768 --decoder-ffn-embed-dim 3072 --decoder-learned-pos --model transformer --batch-size 32 --lr 1e-4 --train-iters 670000 --save transformer.pt --decay-style cosine