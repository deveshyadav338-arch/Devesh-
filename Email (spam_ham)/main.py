from predict import predict_message

if __name__ == "__main__":
    test_message = input("Enter a message: ")
    result = predict_message(test_message)
    print("Prediction:", result)

