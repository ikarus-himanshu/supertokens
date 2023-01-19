import ThirdPartyEmailPassword, { Google, Github, Apple } from "supertokens-auth-react/recipe/thirdpartyemailpassword";
import Session from "supertokens-auth-react/recipe/session";
import EmailVerification from "supertokens-auth-react/recipe/emailverification";


export const SuperTokensConfig = {
    appInfo: {
        appName: "Ikarus_Nest",
        apiDomain: "http://localhost:8000",
        websiteDomain: "http://localhost:3000",
    },
    // recipeList contains all the modules that you want to
    // use from SuperTokens. See the full list here: https://supertokens.com/docs/guides
    recipeList: [
        EmailVerification.init({
            mode: "REQUIRED", // or "OPTIONAL"
          }),

        ThirdPartyEmailPassword.init({  
            getRedirectionURL: async (context) => {
                if (context.action === "SUCCESS") {
                    if (context.redirectToPath !== undefined) {
                        // we are navigating back to where the user was before they authenticated
                        return context.redirectToPath;
                    }
                    return "/";
                }
                return undefined;
            }
            ,
            signInAndUpFeature: {
                signUpForm: {
                    formFields: [{
                        id: "name",
                        label: "Full name",
                        placeholder: "First name and last name"
                    }, {
                        id: "age",
                        label: "Your age",
                        placeholder: "How old are you?",
                    }, {
                        id: "country",
                        label: "Your country",
                        placeholder: "Where do you live?",
                        optional: true
                    }]

                },
                providers: [Github.init(), Google.init(), Apple.init()],
            },
        }),
        Session.init(),




    ],
};
