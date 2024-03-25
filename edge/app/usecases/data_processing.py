from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData

def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    try:
        # Перевіряємо, чи значення координати y акселерометра менше або дорівнює 1000
        if agent_data.accelerometer.y <= 1000:
            road_state = "There is no pit"  # Якщо менше або дорівнює, то стан дороги "Немає ями"
        else:
            road_state = "There is a pit"  # Якщо більше, то стан дороги "Є яма"

        # Повертаємо об'єкт з обробленими даними
        return ProcessedAgentData(road_state=road_state, agent_data=agent_data)
    except Exception as e:
        # Якщо виникає будь-яка помилка, виводимо повідомлення про помилку
        print(f"Error occurred: {e}")


