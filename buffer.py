from typing import Optional

""" class to handle all logs """


class MemoryBuffer:
    logs: list = []

    @staticmethod
    def create_log(
        text: Optional[str],
        rot_type: Optional[str],
        status: Optional[str],
        write_file: Optional[str] = "",
        read_file: Optional[str] = "",
    ):
        MemoryBuffer.logs.append(
            {
                "text": text,
                "rot_type": rot_type,
                "status": status,
                "write_to_file": write_file,
                "read_from_file": read_file,
            }
        )
