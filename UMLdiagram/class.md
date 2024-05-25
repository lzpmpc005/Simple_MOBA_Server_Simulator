@startuml
left to right direction
class Player {
    <u>account</u>: String
    <u>password</u>: String
    playerLevel: Integer
    experiencePoint: Integer
    winCount: Integer
    loseCount: Integer
    matchmakingRanking: Float
}

class CharacterClass {
    <u>type</u>: String
}

class Character {
    <u>name</u>: String
    player: ForeignKey(Player)
    class_type: ForeignKey(CharacterClass)
    winCount: Integer
    loseCount: Integer
}

class MatchRecord {
    <u>id</u>: Integer
    startTime: DateTime
    duration: Integer
    isValid: Boolean
    winner_character: ForeignKey(Character)
    loser_character: ForeignKey(Character)
    host: ForeignKey(Player)
}

class Message {
    <u>id</u>: Integer
    date: DateTime
    sender: ForeignKey(Player)
    content: Text
}

class Blacklist {
    <u>account</u>: String
    startTime: DateTime
    duration: Integer
    misconduct: String
}

Player "1" --> "0..*" Character
CharacterClass "1" --> "0..*" Character
Character "1" --> "0..*" MatchRecord
Player "1" --> "0..*" MatchRecord
Player "1" --> "0..*" Message
Player "1" --> "0..*" Blacklist


@enduml