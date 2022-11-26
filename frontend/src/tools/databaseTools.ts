import { getAccessToken, URI_BASE } from "./jwtTools";

// Send GET request with JWT token
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

// Mutate database unprotected
// Register/Login
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
    headers: headers,
    method: method,
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
    return await databaseExecute(URI, requestOptions);
  }
  return await databaseExecute(URI, requestOptions);
};

// Mutate database protected
// Register/Login
export const databaseMutateProtected = async (
  URI: string,
  body: BodyInit,
  method: string
) => {
  let accessToken = await getAccessToken();
  let headers: HeadersInit = {
    "Content-Type": "application/json",
    Authorization: String(accessToken),
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
    return await databaseExecute(URI, requestOptions);
  }
  return await databaseExecute(URI, requestOptions);
};

// Execute DB commands, return JSON.
// Canbe used for protected and unprotected methods.
export const databaseExecute = async (URI: string, requestOptions) => {
  console.log(requestOptions);
  try {
    let r: Response = await fetch(`${URI_BASE}${URI}`, requestOptions);
    let rJson: JSON = await r.json();
    if (r.status == 200) {
      return { success: true, response: rJson };
    }
    return { success: false, response: rJson };
  } catch (err) {
    return { success: false, response: err };
  }
};
