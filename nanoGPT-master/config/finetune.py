out_dir = 'out'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = "Finetune_gpt"
wandb_run_name = "Run2"

dataset = "lyrics"
init_from = 'gpt2'

always_save_checkpoint = False

batch_size = 8
gradient_accumulation_steps = 32
max_iters = 4000

learning_rate = 3e-5
decay_lr = False
