from aitextgen import aitextgen

ai = aitextgen(tf_gpt2 = "124M",to_gpu=True)
generated_text = ai.generate(prompt = "once upon a time")