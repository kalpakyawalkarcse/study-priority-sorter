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


def main() :
    print("Welcome to Study Priority Sorter!")
    add_topic()

if __name__ == "__main__":
    main()



