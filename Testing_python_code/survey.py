class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey quiz."""
        print(self.question)

    def store_response(self, new_response):
        """Show a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")