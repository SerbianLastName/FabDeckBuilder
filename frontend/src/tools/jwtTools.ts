// Will make moving to production a lot easier.
export const URI_BASE = "http://localhost:5000/";

// Easier to keep login as it's own function.
export const loginUser = async (username: string, password: string) => {
  let body: FormData = new FormData();
  body.append("username", username);
  body.append("password", password);
  let r: Response = await fetch(`${URI_BASE}login`, {
    method: "POST",
    body: body,
  });
  let rJson: JSON = await r.json();
  if (r.status == 200) {
    let token = rJson["token"];
    setCookies(token);
    return { success: true, response: rJson };
  }
  return { success: false, response: rJson };
};

// Set JWT token with 5 day expiration
// Access/Refresh seems like a hassle with no real security benefits.
export const setCookies = (token: string) => {
  let hours: number = 120;
  let expires: string = new Date(
    Date.now() + hours * 60 * 60 * 1000
  ).toUTCString();
  document.cookie = `Authorization= Bearer ${token}; path=/; expires=${expires}`;
  document.cookie = `Expires=${expires}; path=/; expires=${expires}`;
};

// Get JWT token from cookies, refresh token if it expires within 24 hours.
export const getAccessToken = async () => {
  let expires = document.cookie
    .split("; ")
    .find((row) => row.startsWith("Expires="))
    ?.split("=")[1];
  if (expires == undefined) {
    return;
  }
  let tomorrow: string = new Date(
    Date.now() + 24 * 60 * 60 * 1000
  ).toUTCString();
  let accessToken: string | undefined = document.cookie
    .split("; ")
    .find((row) => row.startsWith("Authorization="))
    ?.split("=")[1];
  if (expires >= tomorrow) {
    console.log("token OK");
    return accessToken;
  }
  console.log("token close to expire");
  let token = await refreshToken(accessToken);
  return token;
};

// Use current JWT token to refresh.
export const refreshToken = async (token) => {
  let headers: HeadersInit = {
    "Content-Type": "application/json",
    Authorization: String(token),
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": String(true),
    "Access-Control-Allow-Methods": "*",
  };
  let requestOptions: RequestInit = {
    headers: headers,
    method: "GET",
  };
  let r: Response = await fetch(`${URI_BASE}users/refresh`, requestOptions);
  let rJson = await r.json();
  if (r.status == 200) {
    setCookies(rJson.token);
    return `Bearer ${rJson.token}`;
  }
};
