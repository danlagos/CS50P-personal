def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer_to_everything(answer)

def answer_to_everything(answer):
    match answer:
        case "42" | "forty-two" | "forty two":
            print("yes")
        case _:
            print("no")
    return answer

main()