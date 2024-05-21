@startuml
participant "Player" as PL
participant "Gateway Server" as GS
participant "User Management Server" as US
participant "Authentication Server" as AS
participant "Main Server" as MS
participant "Database Server" as DB

PL -> GS : Register
GS -> AS : Forward Request
AS -> US : Forward Request
US -> DB : Create New Player Account

PL -> GS : Login
GS -> AS : Forward Request
AS -> US : Forward Request
US -> DB : Verify Player

PL -> GS : Update Profile
GS -> AS : Forward Request
AS -> US : Forward Request
US -> DB : Update Profile

PL -> GS : Create Character
GS -> AS : Forward Request
AS -> US : Forward Request
US -> DB : Create Character

PL -> GS : Send Message
GS -> MS : Request for Dynamic Communication
MS -> MS : Build and Maintain Connection
MS -> MS : Receive and Broadcast Message

PL -> GS : Start Match
GS -> MS : Request for Dynamic Communication
MS -> MS : Build and Maintain Connection
MS -> MS : Receive and Broadcast Message
@enduml