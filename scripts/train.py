from aitextgen import aitextgen

ai = aitextgen(tf_gpt2 = "124M",to_gpu=True)
generated_text = ai.generate(prompt="Once upon a time,", max_length=200, temperature=0.7)
print(generated_text) 