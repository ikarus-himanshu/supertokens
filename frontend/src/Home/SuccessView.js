import CallAPIView from "./CallAPIView";
import GoToSiteView from "./GoToSiteView";


export default function SuccessView(props: { userId: string }) {
    let userId = props.userId;

    return (
        <div
            className="fill"
            style={{
                width: "100%",
                alignItems: "center",
                justifyContent: "center",
                textAlign: "center",
                fontWeight: "bold",
                color: "#333333",
                paddingTop: "10px",
                paddingBottom: "40px",
            }}
        >
            <span
                style={{
                    fontSize: "50px",
                }}
            >
                🥳🎉
            </span>
            Login successful
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            Your user ID is
            <div />
            {userId}
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <CallAPIView />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <GoToSiteView />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            {/* <div  className="sessionButton">
            <a href="http://localhost:8000/change_pass" >Change Password</a>
        </div> */}
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            ------------------------------------
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
            <div style={{ height: "10px" }} />
        </div>
    );
}
