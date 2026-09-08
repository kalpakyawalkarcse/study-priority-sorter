import json 
from datetime import date 

def load_topics():
    try : 
        with open('data/topics.json', 'r') as file:
            topics = json.load(file)
            return topics
    except :
        return [] 

def save_topics(topics) :
    with open('data/topics.json', 'w') as file:
        json.dump(topics, file, indent=4) 

def add_topic():
    print("\n---- Add a New Topic ---")
    subject = input("Enter the subject: ")
    topic_name = input("Enter the topic name: ")
    importance = int(input("Enter the importance (1-5): "))
    difficulty = int(input("Enter the difficulty (1-5): "))

    today = str(date.today())
    new_topic = {
        "subject": subject,
        "topic_name": topic_name,
        "importance": importance,
        "difficulty": difficulty,
        "last_Studied": today
    }
    topics = load_topics()
    topics.append(new_topic) 
    save_topics(topics) 

    print("\nTopic added successfully!")

def view_topics():
    print("\n---- View Topics ----")
    topics = load_topics()
    if len(topics) == 0:
        print("No topics saved yet.")
        return
    num = 1 
    for topic in topics:
        print("\nTopic number:", num)
        print("Subject:", topic["subject"])
        print("Topic:", topic["topic_name"])
        print("Importance:", topic["importance"])
        print("Difficulty:", topic["difficulty"])
        print("Last Studied:", topic["last_Studied"])
        num = num + 1   


def main() :
    print("Welcome to Study Priority Sorter!")
    print("1. Add a new topic")
    print("2. View all topics")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        add_topic()
    elif choice == "2":
        view_topics()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



