export async function fetchFromApi(url : string) {
    const data = await fetch(url);
    return data.json();
}