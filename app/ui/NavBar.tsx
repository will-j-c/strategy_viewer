import Link from 'next/link'

interface NavButtonConfig {
  name: string,
  href: string,
}

const navigation: NavButtonConfig[] = [
  { name: 'Dashboard', href: '/' },
  { name: 'Pairs', href: '/pairs' },
  { name: 'Squeeze', href: '/squeeze' },
]

export default function NavBar() {
  return (
    <div className="">
      <ul className="flex flex-row gap-5">
        {navigation.map((item, index) => (
          <Link key={index} href={item.href}>
            <li key={index}>{item.name}</li>
          </Link>
        ))}
      </ul>
    </div>
  )
}
