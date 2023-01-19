import "./App.css";
import SuperTokens, { SuperTokensWrapper, getSuperTokensRoutesForReactRouterDom } from "supertokens-auth-react";
import { SessionAuth } from "supertokens-auth-react/recipe/session";
import { Routes, BrowserRouter as Router, Route } from "react-router-dom";
import Home from "./Home";
import { SuperTokensConfig } from "./config";

import { signOut } from "supertokens-auth-react/recipe/thirdpartyemailpassword";
import { redirectToAuth } from "supertokens-auth-react";
import { useSessionContext } from 'supertokens-auth-react/recipe/session'; 


SuperTokens.init(SuperTokensConfig);


function NavBar() {
    async function onLogout() {
      await signOut();
      window.location.href = "/";
    }
    return (
      <ul>
        <li>Home</li>
        <li onClick={onLogout}>Logout</li>
  
      </ul>
    )
  }

  function Dashboard(props) {
    let session = useSessionContext();

    if (session.loading) {
        return null;
    }

    let {doesSessionExist, userId, accessTokenPayload} = session;

    // doesSessionExist will always be true if this is wrapped in `<SessionAuth>`
    if (!doesSessionExist) {
        // TODO
    }

    let name = accessTokenPayload.userName;
}

function App() {
    return (
        <SuperTokensWrapper>
            <div className="App">
                <Router>
                    <div className="fill">
                        <Routes>
                            {/* This shows the login UI on "/auth" route */}
                            {getSuperTokensRoutesForReactRouterDom(require("react-router-dom"))}

                            <Route
                                path="/"
                                element={
                                    /* This protects the "/" route so that it shows
                                  <Home /> only if the user is logged in.
                                  Else it redirects the user to "/auth" */
                                    <SessionAuth>
                                        <Home />
                                    </SessionAuth>
                                }
                            />
                        </Routes>
                    </div>
                </Router>
            </div>
        </SuperTokensWrapper>
    );
}

export default App;
