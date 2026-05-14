const WebSocket = require("ws");

const gateway = new WebSocket("wss://gateway.discord.gg/?v=10&encoding=json");

gateway.on("open", () => {
    console.log("Connected to Discord Gateway");
});

gateway.on("message", (data) => {
    const event = JSON.parse(data);

    // Отримання нових повідомлень
    if (event.t === "MESSAGE_CREATE") {
        console.log("New message:", event.d.content);
    }
});

gateway.on("close", () => {
    console.log("Connection closed");
});
