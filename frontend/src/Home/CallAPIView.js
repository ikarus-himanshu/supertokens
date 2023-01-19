import axios from "axios";

export default function CallAPIView() {
    async function callAPIClicked() {
        let response = await axios.get("http://localhost:8000/get_user_info_api");
        window.alert("Session Information:\n" + JSON.stringify(response.data, null, 2));
    }

    return (
        <div onClick={callAPIClicked} className="sessionButton">
            Get Session Info
        </div>
    );
}
