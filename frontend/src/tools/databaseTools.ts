export const databaseGetProtected = async (URI: string) => {
  let accessToken = await getAccessToken();
  let headers: HeadersInit = {
    "Content-Type": "application/json",
    Authorization: String(accessToken),
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": String(true),
    "Access-Control-Allow-Methods": "*",
  };
  let requestOptions: RequestInit = {
    headers: headers,
    method: "GET",
  };
  return await databaseExecute(URI, requestOptions);
};

export const databaseMutate = async (
  URI: string,
  body: BodyInit,
  method: string
) => {
  let headers: HeadersInit = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": String(true),
    "Access-Control-Allow-Methods": "*",
  };
  let requestOptions: RequestInit = {
    method: method,
    headers: headers,
    body: body,
  };
  if (method == "DELETE") {
    let headers: HeadersInit = {
      "Content-Type": "application/json",
    };
    let requestOptions: RequestInit = {
      method: method,
      headers: headers,
    };
    return databaseExecute(URI, requestOptions);
  }
  return databaseExecute(URI, requestOptions);
};

export const databaseExecute = async (URI: string, requestOptions) => {
  try {
    let r: Response = await fetch(URI, requestOptions);
    let rJson: JSON = await r.json();
    if (r.status == 200) {
      return { success: true, response: rJson };
    }
    return { success: false, response: rJson };
  } catch (err) {
    return { success: false, response: err };
  }
};

export const loginUser = async (username: string, password: string) => {
  let body: FormData = new FormData();
  body.append("username", username);
  body.append("password", password);
  let r: Response = await fetch("http://localhost:5000/login", {
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

export const setCookies = (token: string) => {
  let hours: number = 120;
  let expires: string = new Date(
    Date.now() + hours * 60 * 60 * 1000
  ).toUTCString();
  document.cookie = `Authorization= Bearer ${token}; path=/; expires=${expires}`;
  document.cookie = `Expires=${expires}; path=/; expires=${expires}`;
};

export const getAccessToken = async () => {
  let expires = document.cookie
    .split("; ")
    .find((row) => row.startsWith("Expires="))
    ?.split("=")[1];
  if (expires == undefined) return;
  let tomorrow: string = new Date(
    Date.now() + 24 * 60 * 60 * 1000
  ).toUTCString();
  let accessToken: string | undefined = document.cookie
    .split("; ")
    .find((row) => row.startsWith("Authorization="))
    ?.split("=")[1];
  if (expires <= tomorrow) {
    return accessToken;
  }
  let token = await refreshToken(accessToken);
  return token;
};

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
  let URI: string = "http://localhost:5000/users/refresh";
  let r: Response = await fetch(URI, requestOptions);
  let rJson = await r.json();
  console.log(rJson);
  if (r.status == 200) {
    setCookies(rJson.token);
    return `Bearer ${rJson.token}`;
  }
};
