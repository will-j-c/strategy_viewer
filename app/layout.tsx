import NavBar from "./ui/NavBar";
import "./globals.css";


export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body
        className={"antialiased"}
      >
        <NavBar />
        <main>
          {children}
        </main>
      </body>
    </html>
  );
}
