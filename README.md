This Audio File API is a Django Rest Framework API that simulates the behavior of an audio file server
while using Postgres as the Database.

The audio files can be of 3 types, with structures as shown below:
– Song
– Podcast
– Audiobook

Song file fields:
- ID – (mandatory, integer, unique)
- Name of the song – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

Podcast file fields:
- ID – (mandatory, integer, unique)
- Name of the podcast – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)
- Host – (mandatory, string, cannot be larger than 100 characters)
- Participants – (optional, list of strings, each string cannot be larger than
100 characters, maximum of 10 participants possible)

Audiobook file fields:
- ID – (mandatory, integer, unique)
- Title of the audiobook – (mandatory, string, cannot be larger than 100
characters)
- Author of the title (mandatory, string, cannot be larger than 100
characters)
- Narrator - (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

The API Endpoints implemented are:
- Create API:
    The request has the following fields:
    - audioFileType – mandatory, one of the 3 audio types possible
    - audioFileMetadata – mandatory, dictionary, contains the metadata for one
    of the three audio files (song, podcast, audiobook)

    "/create" 

- Delete API:
    `/delete/{<audioFileType>}/{<audioFileID>}` e.g. "delete/Song/1"

- Update API:
    `/update/{<audioFileType>}/{<audioFileID>}` e.g. "update/Podcast/2"

- Get API:
    `/{<audioFileType>}/{<audioFileID>}` e.g. "get/Song/1"

- GetAll API:
    `/{<audioFileType>}` e.g "get/Audiobook/1"

