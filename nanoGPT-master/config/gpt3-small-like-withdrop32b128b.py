# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 20
log_interval = 1 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = True # override via command line if you like
wandb_project = 'data309gptnew'
wandb_run_name = 'Gpt3likewithdrop32batch128block'

dataset = 'lyrics'
gradient_accumulation_steps = 1
batch_size = 32 # TO BE PROPERLY DETERMINED
block_size = 128 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 12
n_head = 12
n_embd = 768
dropout = 0.1

learning_rate = 6.0e-4 # with baby networks can afford to go a bit higher
max_iters = 4000
lr_decay_iters = 4000# make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
device = 'cuda' 
# compile = False # do not torch compile the model
