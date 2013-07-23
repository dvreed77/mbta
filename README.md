# Playing with MBTA data

## Installation

Documentation is [here] [1], but isn't super clear.  Here is what I have been able to do.

1. download [protbuf] [2], a Google project to encode structured data efficiently.  This is important because this is realtime data, and was primarily given as XML files which are easy to read, but not that efficient.  This is a new happy medium.
2. you are going to need a [.proto] [3] file. Simply, a .proto file is a format file that descibes how the .pb binary file is organized, seems like a cool idea. For transit, this has also been generated by google. This was a bit confusing at first, cause I thought this would be generated by MBTA, but it looks like they are being smart and using a common format.
3. Next you need to compile the .proto file into a .py file that you can then use to process your .pb file.  

> protoc --python_out=. gtfs-realtime.proto




[1]: http://realtime.mbta.com/Portal/Content/Documents/MBTA-realtime_DeveloperDocumentation_v1.0.2_2013-06-25.pdf
[2]: https://code.google.com/p/protobuf/downloads/detail?name=protobuf-2.5.0.tar.gz
[3]: https://developers.google.com/transit/gtfs-realtime/gtfs-realtime-proto