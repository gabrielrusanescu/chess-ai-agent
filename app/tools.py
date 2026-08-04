"""
Tools available to the Summer School AI Assistant.

The tools currently access a local Markdown knowledge base.
Later, the same operations will use Google Cloud Storage.
"""

from app.knowledge import KnowledgeProvider


class AssistantTools:
    """Operations that the AI agent can perform on the knowledge base."""

    def __init__(self, knowledge_provider: KnowledgeProvider):
        self.knowledge = knowledge_provider

    def list_documents(self) -> dict:
        """
        List the available knowledge documents.

        Use this tool when the user asks what information, topics,
        files, or workshop materials are available.

        Returns:
            A dictionary containing the operation status and filenames.
        """
        documents = self.knowledge.list_documents()

        return {
            "status": "success",
            "documents": documents,
            "document_count": len(documents),
        }

    def read_document(self, filename: str) -> dict:
        """
        Read a specific document from the knowledge base.

        Use this tool when the user asks about the contents of a known
        document or when another tool identifies a relevant filename.

        Args:
            filename: Exact Markdown filename, such as "day2.md".

        Returns:
            A dictionary containing the document content or an error.
        """
        try:
            content = self.knowledge.read_document(filename)
        except FileNotFoundError:
            return {
                "status": "error",
                "filename": filename,
                "error_message": f"Document '{filename}' was not found.",
            }

        return {
            "status": "success",
            "filename": filename,
            "content": content,
        }
    def append_note(self, filename: str, note: str) -> dict:
        """
        Append a note, comment, or game insight to a Markdown document.

        Use this tool when the user asks to save a thought, add a note about
        an opening, or record details into a knowledge base file.

        Args:
            filename: Target Markdown filename, such as "notes.md" or "openings.md".
            note: The text content to append to the file.

        Returns:
            A dictionary containing the status of the write operation.
        """
        cleaned_note = note.strip()

        if not cleaned_note:
            return {
                "status": "error",
                "filename": filename,
                "error_message": "The note content cannot be empty.",
            }

        try:
            self.knowledge.append_note(filename, cleaned_note)
        except FileNotFoundError:
            return {
                "status": "error",
                "filename": filename,
                "error_message": f"Document '{filename}' was not found.",
            }
        except Exception as error:
            return {
                "status": "error",
                "filename": filename,
                "error_message": f"Could not append to '{filename}': {error}",
            }

        return {
            "status": "success",
            "filename": filename,
            "message": f"Successfully appended note to '{filename}'.",
        }
        
    def search_documents(self, keyword: str) -> dict:
        """
        Search all knowledge documents and return short matching excerpts.

        Use this tool when the user asks which workshop materials mention
        a particular concept, service, command, or technology.

        Args:
            keyword: Word or phrase to search for, such as "Docker".

        Returns:
            A dictionary containing matching filenames and line excerpts.
        """
        normalized_keyword = keyword.strip().casefold()

        if not normalized_keyword:
            return {
                "status": "error",
                "keyword": keyword,
                "error_message": "The search keyword cannot be empty.",
            }

        matches: list[dict] = []

        for filename in self.knowledge.list_documents():
            content = self.knowledge.read_document(filename)
            excerpts: list[dict] = []

            for line_number, line in enumerate(content.splitlines(), start=1):
                if normalized_keyword in line.casefold():
                    excerpts.append(
                        {
                            "line_number": line_number,
                            "text": line.strip(),
                        }
                    )

                if len(excerpts) == 3:
                    break

            if excerpts:
                matches.append(
                    {
                        "filename": filename,
                        "excerpts": excerpts,
                    }
                )

        return {
            "status": "success",
            "keyword": keyword,
            "matches": matches,
            "match_count": len(matches),
        }
