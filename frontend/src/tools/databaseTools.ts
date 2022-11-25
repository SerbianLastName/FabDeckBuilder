export const databaseGet = async (URI: string) => {
  let headers: HeadersInit = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": String(true),
    "Access-Control-Allow-Methods": "*",
  };
  let requestOptions: RequestInit = {
    headers: headers,
    method: "get",
  };
  return databaseExecute(URI, requestOptions);
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

export const databaseExecute = async (
  URI: string,
  requestOptions: RequestInit
) => {
  try {
    let r: Response = await fetch(`${URI}`, requestOptions);
    let rJson: JSON = await r.json();
    if (r.status == 200) {
      return { success: true, return: rJson };
    }
    return { success: false, return: rJson };
  } catch (err) {
    let errJson: JSON = await err.json();
    return { success: false, return: errJson };
  }
};
