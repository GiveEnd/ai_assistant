import gradio as gr

# Пока пустая функция, где, предположительно, будет логика создания описания
def generate_description(description):
    return "Когда-нибудь здесь будет красивое описание"


# Обращение к ai
def chat_response(user_message):
    return 'Ваше описание: ' + generate_description(user_message)


# Набор блоков. Блоки нужны, чтобы разделять фрагменты разметки. Здесь принцип похож на составление таблиц в бд.
# Blocks - как бы таблица. Rows - её строки. Columns - столбцы.
with gr.Blocks() as app:
    # Строка содержащая два основных элемента - интерфейс карточки и интерфейс чата.
    with gr.Row():
        # Первый блок - интерфейс карточки.
        with gr.Column(scale=1):
            gr.Markdown("### 🏨 Карточка отеля")
            name = gr.Textbox(label="Название отеля", placeholder="Введите название отеля")
            address = gr.Textbox(label="Адрес", placeholder="Введите адрес отеля")
            description = gr.Textbox(label="Описание", placeholder="Введите краткое описание...", lines=4)
            gr.Markdown("Загрузите одну или несколько фотографий отеля.")
            photos = gr.Image(label="Фотографии отеля")

        # Второй блок - интерфейс чата.
        with gr.Column(scale=1):
            gr.Markdown("### 💬 Чат")
            chatbot = gr.Chatbot(
                label="Чат с ассистентом",
                value=[
                    {"role": "assistant", "content": "Здравствуйте! Чем могу помочь в описании вашего отеля?"}
                ],
                height=650,
                type="messages"
            )
            message = gr.Textbox(label="Ваш вопрос", placeholder="Спросите что-то о создании описания...")
            send_button = gr.Button("Отправить")


        # Обработка события нажатия на кнопку "Отправить"
        def respond(user_message, chat_history):
            bot_response = chat_response(user_message)
            chat_history.append({"role": "user", "content": user_message})
            chat_history.append({"role": "assistant", "content": bot_response})
            return chat_history, ""


        # Вызов события при нажати на кнопку "Отправить"
        send_button.click(respond, inputs=[message, chatbot], outputs=[chatbot, message])

app.launch()