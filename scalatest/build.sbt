lazy val root = (project in file(".")).
    settings(
        name := "hello",
        version := "0.1",
        scalaVersion := "2.11.8"
    )

libraryDependencies ++= Seq(
    "com.typesafe.akka" %% "akka-http-core" % "10.0.0",
    "com.typesafe.akka" %% "akka-http" % "10.0.0",
    "com.typesafe.akka" %% "akka-http-testkit" % "10.0.0",
    "com.typesafe.akka" %% "akka-http-spray-json" % "10.0.0",
    "com.typesafe.akka" %% "akka-http-jackson" % "10.0.0",
    "com.typesafe.akka" %% "akka-http-xml" % "10.0.0"
)
