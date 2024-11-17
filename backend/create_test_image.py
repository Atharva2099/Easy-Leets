from PIL import Image, ImageDraw

def create_graph_image():
    # Create a white image
    width, height = 800, 600
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw some nodes and edges for a graph problem
    nodes = [
        (200, 200), (400, 200), (600, 200),  # Row 1
        (200, 400), (400, 400), (600, 400)   # Row 2
    ]
    
    # Draw edges with weights
    edges = [
        (0, 1, "5"), (1, 2, "3"),   # Top row
        (3, 4, "4"), (4, 5, "6"),   # Bottom row
        (0, 3, "2"), (1, 4, "7"), (2, 5, "4")  # Vertical connections
    ]
    
    # Draw edges with weights
    for start_idx, end_idx, weight in edges:
        start = nodes[start_idx]
        end = nodes[end_idx]
        draw.line([start, end], fill='black', width=2)
        draw.text((
            (start[0] + end[0]) // 2,
            (start[1] + end[1]) // 2
        ), weight, fill='red')
    
    # Draw nodes
    for i, (x, y) in enumerate(nodes):
        # White circle with black border
        draw.ellipse([x-20, y-20, x+20, y+20], outline='black', fill='white', width=2)
        draw.text((x-5, y-5), str(i), fill='black')
    
    # Add problem description
    draw.text((10, 10), "Find the shortest path from node 0 to node 5", fill='black')
    
    # Save the image
    image.save('test.png')
    print("Created test.png with shortest path problem")

if __name__ == "__main__":
    create_graph_image()