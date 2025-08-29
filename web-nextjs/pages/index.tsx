import Head from 'next/head'

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-100 to-purple-200">
      <Head>
        <title>Cognate</title>
        <meta name="description" content="AI-Powered Learning Ecosystem" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
        <h1 className="text-6xl font-bold">
          Welcome to{' '}
          <a className="text-blue-600" href="https://nextjs.org">
            Cognate!
          </a>
        </h1>

        <p className="mt-3 text-2xl">
          Your personalized AI learning companion.
        </p>

        <div className="flex flex-wrap items-center justify-around max-w-4xl mt-6 sm:w-full">
          <a
            href="#"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-blue-600 focus:text-blue-600"
          >
            <h3 className="text-2xl font-bold">Dashboard &rarr;</h3>
            <p className="mt-4 text-xl">
              View your adaptive schedule and track your progress.
            </p>
          </a>

          <a
            href="#"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-blue-600 focus:text-blue-600"
          >
            <h3 className="text-2xl font-bold">Career Coach &rarr;</h3>
            <p className="mt-4 text-xl">
              Get AI-powered career and skill recommendations.
            </p>
          </a>

          <a
            href="#"
            className="p-6 mt-6 text-left border w-96 rounded-xl hover:text-blue-600 focus:text-blue-600"
          >
            <h3 className="text-2xl font-bold">Peer Learning &rarr;</h3>
            <p className="mt-4 text-xl">
              Connect with peers and study groups worldwide.
            </p>
          </a>
        </div>
      </main>
    </div>
  )
}
