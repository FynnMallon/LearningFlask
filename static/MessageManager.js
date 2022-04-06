class Message{
    constructor(Sender,Message,TimeStamp){
        this.Sender = Sender
        this.Message = Message
        this.TimeStamp = TimeStamp
    }
    BuildHtml(){
        var Top = document.getElementById("Messages");
        const ThisMsg = document.createElement("div")
        ThisMsg.classList.add("container")
        const id = 0
        ThisMsg.id = (id)
        Top.appendChild(ThisMsg)
        const TextElement = document.createElement("p")
            const Text = document.createTextNode(this.Message)
                TextElement.appendChild(Text)
        const TimeHolder = document.createElement("span")
            TimeHolder.innerHTML = this.TimeStamp
        const location = document.getElementById("0")
            location.appendChild(TextElement)
            location.appendChild(TimeHolder)
    }
}

let Message1 = new Message("Fynn", "Hello", "12:57")
Message1.BuildHtml()

function Establish (data){
    const ArrayofData = data
    alert(ArrayofData[0])
}