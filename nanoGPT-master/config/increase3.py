# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 20
log_interval = 1 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = True # override via command line if you like
wandb_project = 'data309gpt'
wandb_run_name = 'BaseLineTrain'

dataset = 'lyrics'
gradient_accumulation_steps = 2
batch_size = 128
block_size = 512 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 32
n_head = 32
n_embd = 1024
dropout = 0.0

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 16000
lr_decay_iters = 16000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 400 # not super necessary potentially

# on macbook also add
device = 'cuda' 
# compile = False # do not torch compile the model
