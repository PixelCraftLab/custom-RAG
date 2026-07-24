MAX_HISTORY = 40

conversation_history = []
# print(conversation_history)


def add_user_message(message: str):
    conversation_history.append(
        {
            "role": "user",
            "content": message,
        }
    )

def add_retrieved_chunks(results):
    """
    Stores the retrieved chunks in the conversation history.

    results should be the output of:
    similarity_search_with_score()
    """

    chunks = []

    for doc, score in results:
        chunks.append(
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": score,
            }
        )

    conversation_history.append(
        {
            "role": "retrieval",
            "chunks": chunks,
        }
    )

    trim_history()


def add_assistant_message(message: str):
    conversation_history.append(
        {
            "role": "assistant",
            "content": message,
        }
    )

    trim_history()


def trim_history():
    """
    Keeps only the latest MAX_HISTORY messages.
    """

    global conversation_history

    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]


def get_conversation():
    return conversation_history


def clear_conversation():
    conversation_history.clear()

# MAX_HISTORY = 50

# conversation_history = []


# def add_user_message(message: str):
#     conversation_history.append(
#         {
#             "role": "user",
#             "content": message,
#         }
#     )
 
#     trim_history()


# def add_retrieved_chunks(results):
#     """
#     Stores the retrieved chunks in the conversation history.

#     results should be the output of:
#     similarity_search_with_score()
#     """

#     chunks = []

#     for doc, score in results:
#         chunks.append(
#             {
#                 "content": doc.page_content,
#                 "metadata": doc.metadata,
#                 "score": score,
#             }
#         )

#     conversation_history.append(
#         {
#             "role": "retrieval",
#             "chunks": chunks,
#         }
#     )

#     trim_history()


# def add_assistant_message(message: str):
#     conversation_history.append(
#         {
#             "role": "assistant",
#             "content": message,
#         }
#     )

#     trim_history()


# def trim_history():
#     global conversation_history

#     if len(conversation_history) > MAX_HISTORY:
#         conversation_history = conversation_history[-MAX_HISTORY:]


# def get_conversation():
#     return conversation_history


# def clear_conversation():
#     conversation_history.clear()