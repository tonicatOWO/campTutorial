fn main() {
    let a: i32 = 65;
    // let c: char = a;    // 編譯錯誤！不允許隱式轉換
    let c: char = char::from(a as u8); // 必須明確安全轉換
    println!("{}", c); // 輸出: A
}
