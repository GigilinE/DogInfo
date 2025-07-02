# -*- coding: utf-8 -*-

def migrate(cr, version):
    """Migrate data from x_studio_dog_* fields to dog_* fields"""
    
    # Check if old fields exist and copy data to new fields
    cr.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = 'res_partner' 
        AND column_name IN ('x_studio_dog_name', 'x_studio_dog_breed', 'x_studio_dog_age', 'x_studio_dog_weight')
    """)
    
    existing_fields = [row[0] for row in cr.fetchall()]
    
    if existing_fields:
        # Copy data from old fields to new fields
        field_mapping = {
            'x_studio_dog_name': 'dog_name',
            'x_studio_dog_breed': 'dog_breed',
            'x_studio_dog_age': 'dog_age',
            'x_studio_dog_weight': 'dog_weight'
        }
        
        for old_field, new_field in field_mapping.items():
            if old_field in existing_fields:
                # Check if new field exists
                cr.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = 'res_partner' 
                    AND column_name = %s
                """, (new_field,))
                
                if cr.fetchone():
                    # Copy data
                    cr.execute(f"""
                        UPDATE res_partner 
                        SET {new_field} = {old_field} 
                        WHERE {old_field} IS NOT NULL
                    """)
                    
        # Drop old fields
        for old_field in existing_fields:
            cr.execute(f"ALTER TABLE res_partner DROP COLUMN IF EXISTS {old_field}")