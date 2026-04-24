import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SimplePID(Node):
    def __init__(self):
        super().__init__('pid_controller')
        self.target_speed = 100.0
        self.current_speed = 0.0
        
        # Coefficients PID
        self.Kp = 0.5
        self.Ki = 0.1
        self.Kd = 0.05
        
        self.error_sum = 0.0
        self.last_error = 0.0

        self.publisher_ = self.create_publisher(Float32, 'motor_command', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

    def control_loop(self):
        error = self.target_speed - self.current_speed
        self.error_sum += error
        error_diff = error - self.last_error
        
        # Calcul de la commande
        u = (self.Kp * error) + (self.Ki * self.error_sum) + (self.Kd * error_diff)
        
        # Simulation d'une réponse moteur simple
        self.current_speed += u * 0.1 
        
        msg = Float32()
        msg.data = self.current_speed
        self.publisher_.publish(msg)
        self.get_logger().info(f'Target: {self.target_speed} | Current: {self.current_speed:.2f}')
        self.last_error = error

def main(args=None):
    rclpy.init(args=args)
    node = SimplePID()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
