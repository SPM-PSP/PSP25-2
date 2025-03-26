<template>
    <div class="chat-container">
        <div class="chat-box" v-for="(message, index) in messages" :key="index">
            <div :class="['chat-bubble', message.sender]">
                {{ message.text }}
            </div>
        </div>
        <div class="input-container">
            <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your question here..." />
            <button @click="sendMessage">Send</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userInput: '',
            messages: []
        };
    },
    methods: {
        async sendMessage() {
            if (this.userInput.trim() === '') return;

            // Add user message to chat
            this.messages.push({ text: this.userInput, sender: 'user' });

            // Simulate sending message to language model and receiving a response
            const response = await this.getResponseFromModel(this.userInput);

            // Add model response to chat
            this.messages.push({ text: response, sender: 'model' });

            // Clear input field
            this.userInput = '';
        },
        async getResponseFromModel(question) {
            // Simulate an API call to a language model
            // Replace this with actual API call
            return new Promise((resolve) => {
                setTimeout(() => {
                    resolve(`Response to: ${question}`);
                }, 1000);
            });
        }
    }
};
</script>

<style>
.chat-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    padding: 10px;
}

.chat-box {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
}

.chat-bubble {
    max-width: 60%;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}

.chat-bubble.user {
    align-self: flex-end;
    background-color: #d1e7dd;
}

.chat-bubble.model {
    align-self: flex-start;
    background-color: #f8d7da;
}

.input-container {
    display: flex;
    margin-top: auto;
}

input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px;
    margin-left: 10px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}
</style>