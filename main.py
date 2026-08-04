from pathlib import Path

from app.knowledge import LocalKnowledgeProvider
from app.tools import AssistantTools


def main() -> None:
    """Demonstrate the local knowledge tools without using Google Cloud."""

    print("\n=== Chess AI Assistant ===\n")

    provider = LocalKnowledgeProvider(Path("knowledge"))
    tools = AssistantTools(provider)

    print("Available documents")
    print("-------------------")

    documents_result = tools.list_documents()

    for document in documents_result["documents"]:
        print(f"- {document}")

    print(f"\nTotal documents: {documents_result['document_count']}")

    print("\nReading rules_and_setup.md")
    print("-------------------")

    reading_result = tools.read_document("rules_and_setup.md")

    if reading_result["status"] == "success":
        print(reading_result["content"])
    else:
        print(reading_result["error_message"])

    print("\nSearching for 'castling'")
    print("----------------------")

    search_result = tools.search_documents("castling")

    if search_result["status"] == "error":
        print(search_result["error_message"])
        return

    if not search_result["matches"]:
        print("No documents found.")
        return

    for match in search_result["matches"]:
        print(f"\n{match['filename']}")

        for excerpt in match["excerpts"]:
            print(
                f"  line {excerpt['line_number']}: "
                f"{excerpt['text']}"
            )
    print("\nAppending note to rules_and_setup.md")
    print("-----------------------------------")

    note_result = tools.append_note(
        "rules_and_setup.md",
        "Note: En passant must be executed on the turn immediately following the opponent's pawn move."
    )

    if note_result["status"] == "success":
        print(note_result["message"])
    else:
        print(note_result["error_message"])


if __name__ == "__main__":
    main()
