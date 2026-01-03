from rdco_agent_system.agents.orchestration_agent import OrchestrationAgent

def main():
    """
    Main function to run the RD&Co Multi-Agent System.
    """
    print("Initializing RD&Co Multi-Agent System...")
    orchestrator = OrchestrationAgent()
    print("\nSystem ready. You can start sending requests.")
    print("Type 'exit' or 'quit' to terminate.")

    while True:
        try:
            # Get user input from the command line
            user_input = input("\n[User]> ")

            if user_input.lower() in ["exit", "quit"]:
                print("Terminating the system. Goodbye!")
                break

            if not user_input:
                continue

            # Handle the request using the orchestrator
            response = orchestrator.handle_request(user_input)

            # Print the system's response
            print("\n[RD&Co Agent System]>")
            print(response)

        except KeyboardInterrupt:
            print("\n\nInterrupted by user. Terminating...")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            # In a real system, you'd have more robust error handling.
            # For now, we'll just continue the loop.
            continue

if __name__ == "__main__":
    main()
