import axios from "axios";

export default function CallAPIView() {
    async function callAPIClicked() {
        window.location = "http://localhost:8000/";
    }

    return (
        <div onClick={callAPIClicked} className="sessionButton">
            Go To Ikarus_Nest
        </div>
    );
}
