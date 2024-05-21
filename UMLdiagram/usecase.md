@startuml
left to right direction

actor "Player" as PL
actor "Gateway Server" as GS
actor "User Management Server" as US
actor "Authentication Server" as AS
actor "Main Server" as MS
actor "Database Server" as DB



rectangle "Web Mutiplayer System" {



  rectangle "Frontend"{

    usecase "Request for Static Response"
    usecase "Request for Dynamic Communication"
  
    rectangle "Registration Page"{
      usecase "Register"
      usecase "Login"
   }
  
 
    rectangle "Playing Space"{
      usecase "Send Message"
      usecase "Start Match"
   }

    rectangle "Player Profile"{
      usecase "Create Character"
      usecase "Update Profile"
   }

  
   
 }

  rectangle "Backend"{
    usecase "Forward Request"
  
    rectangle "Real-time Processing"{
      
      usecase "Build and Maintain Connection"
      usecase "Receive and Broadcast Message"
      usecase "Create Record"
  
    }

    rectangle "Non-real-time Processing"{


      usecase "Create New Player Account"
      usecase "Verify Player"

  
    }
   
 }


PL -- "Register"
PL -- "Login"

PL -- "Update Profile"
PL -- "Create Character"

"Login" -- "Request for Static Response"
"Register"  -- "Request for Static Response"
"Update Profile"  -- "Request for Static Response"
"Create Character"  -- "Request for Static Response"

"Request for Static Response" -- GS
GS -- "Forward Request"

"Forward Request" -- AS
"Forward Request" -- US

US -- "Create New Player Account"
AS -- "Verify Player"

"Create New Player Account" -- DB
"Verify Player" -- DB



PL -- "Send Message"
PL -- "Start Match"

"Send Message" -- "Request for Dynamic Communication"
"Start Match" -- "Request for Dynamic Communication"

"Request for Dynamic Communication" -- MS

MS -- "Build and Maintain Connection"
MS -- "Receive and Broadcast Message"
MS -- "Create Record"

"Create Record" -- DB

}
@enduml