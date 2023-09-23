import g4f

# print(g4f.Provider.Theb.params)  # supported args

# Automatic selection of provider

# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "tell me something funny"}
    ],
)
print("message: ", response, "\n\n")
for message in response:
    print(message, flush=True, end="")
print("#" * 100)

# # normal response
# response = g4f.ChatCompletion.create(
#     model=g4f.models.gpt_4,
#     messages=[{"role": "user", "content": "Give me some quotes from the book  Left Behind by Tim LaHaye"}],
# )  # alterative model setting

# print(response)
# print('#'*100)


# # Set with provider
# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     provider=g4f.Provider.DeepAi,
#     messages=[{"role": "user", "content": "Give me some quotes from the book  Left Behind by Tim LaHaye"}],
#     stream=True,
# )

# for message in response:
#     print(message)
